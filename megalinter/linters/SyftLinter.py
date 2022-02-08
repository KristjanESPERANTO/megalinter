#!/usr/bin/env python3
"""
Use Syft to generate SBOM (Software bill of materials)
"""

import json
import logging
import os

from megalinter import Linter


class SyftLinter(Linter):

    # Get syft json output and build SARIF output from it
    def manage_sarif_output(self, _return_stdout):
        if self.can_output_sarif is True and self.output_sarif is True:
            json_output_file = f"{self.sarif_output_file}.syft.json"
            if os.path.isfile(json_output_file):
                with open(json_output_file, "r", encoding="utf-8") as json_file:
                    json_file_str = json_file.read()
                    if logging.getLogger().isEnabledFor(logging.DEBUG):
                        logging.debug("SYFT initial output file: " + json_file_str)
                    syft_result_sbom = json.loads(json_file_str)
                sarif_obj = {
                    "$schema": "https://schemastore.azurewebsites.net/schemas/json/sarif-2.1.0-rtm.5.json",
                    "properties": {
                        "comment": "Generated by MegaLinter for syft",
                        "docUrl": "https://megalinter.github.io/v6-alpha",
                    },
                    "runs": [
                        {
                            "tool": {
                                "driver": {
                                    "informationUri": "https://github.com/anchore/syft",
                                    "name": "syft",
                                    "rules": [
                                        {
                                            "id": "SYFT_SBOM",
                                            "name": "sbom_generation",
                                            "shortDescription": {
                                                "text": "Generate Software Bill Of Materials"
                                            },
                                        },
                                    ],
                                }
                            },
                            "results": [
                                {
                                    "level": "note",
                                    "properties": {"sbom": syft_result_sbom},
                                    "message": {"text": "Generated SBOM"},
                                    "ruleId": "SYFT_SBOM",
                                }
                            ],
                        }
                    ],
                    "version": "2.1.0",
                }
                with open(self.sarif_output_file, "w", encoding="utf-8") as outfile:
                    json.dump(sarif_obj, outfile, indent=4, sort_keys=False)
                    outfile.write("\n")