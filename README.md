# COL metadata

Metadata.yaml files for all sources of COL. Each folder (named by the current alias or key if missing) contains the following files:

 - {key}-latest.yaml: the current metadata of the latest version imported into ChecklistBank
 - {key}-archived.yaml (optional): The metadata as it is currently archived for the source in the project, according to the last time the data was synced. This file will only be created when the latest version differs and is based on a newer import that is currently used in the project.
 - {key}-patch.yaml (optional): the patch if it exists
 - attempts.txt: in case the archived.yaml exists this file lists both import attempts (latest & archived)