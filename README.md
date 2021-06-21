# COL metadata

Metadata.yaml files for all sources of COL. Each folder (named by the current alias or key if missing) contains the following files:

 - `{key}-latest.yaml`: the current metadata of the latest version imported into ChecklistBank
 - `{key}-archived.yaml` (optional): The metadata as it is currently archived for the source in the project, according to the last time the data was synced. This file will only be created when the latest version differs and is based on a newer import that is currently used in the project.
 - `{key}-patch.yaml` (optional): the patch if it exists
 - `attempts.txt` (optional): in case the archived.yaml exists this file lists both import attempts (latest & archived)


## Splitting up the Work
Review of the metadata will be split up by dataset name between

 - Yuri: 3i - F
 - Geoff: G-P
 - Olaf: R-S
 - Chantal: T-World Plants

## Editing
The latest.yaml file can be edited in any plain text editor.
Suggest TextMate or SublimeText on a Max, xxx on Windows.

## Validation
You can check the validity of the YAML files here:
https://data.dev.catalogueoflife.org/tools/metadata-validator

## Update data in github
Send the modified latest.yaml file with the name of the alias to Markus, who will merge it into the repository again.

