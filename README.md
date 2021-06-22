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

## Editing in Visual Studio Code
The latest.yaml file can be edited in any plain text editor like [TextMate](https://macromates.com) on a Max or [Notepad++](https://notepad-plus-plus.org) on Windows.
We recommend [Visual Studio Code](https://code.visualstudio.com) though, because it can validate the YAML to our [JSON schema](https://github.com/CatalogueOfLife/coldp/blob/master/metadata.json) and provide editing suggestions. It is freely available for both Mac & Windows.

### Setting up VS Code
Based on https://scottaddie.com/2016/08/02/community-driven-json-schemas-in-visual-studio-2015/

In order to validate the yaml files we need to tell VS Code where our JSON schema is.
This can be done on the VS Code Settings page.
As we are creating a Schema for a YAML file, make sure you have the [YAML Extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) installed before continuing.

First, download the `metadata.json` file to your local machine:
https://github.com/CatalogueOfLife/coldp/blob/master/metadata.json

Then, go to Code/File -> Preferences -> Settings (or use the Command Pallete) to open the settings page and search for yaml.
Open the settings for the YAML extension and search for "Yaml: Schemas" and click "Edit in settings.json".

![settings.png](https://res.cloudinary.com/practicaldev/image/fetch/s--yB3ULfC3--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/cjyo0kkogh1dnf8s3y1y.png)

The "settings.json" file will open. If it doesn´t exist yet, you will have to create it.

Copy the following yaml and suggest settings to your VSCode settings. This will enable validation and auto suggestion for COL metadata for the `-latest.yaml` and `-patch.yaml` files. On a mac it looks like this in my case. You will need to udpate to your local schema path:

```
    "javascript.suggest.names": false,
    "editor.suggest.showWords": false,
    "yaml.schemas": {
        "/Users/markus/Downloads/metadata.json": ["*-latest.yaml", "*-patch.yaml"],
    },
    "yaml.disableAdditionalProperties": true,
    "yaml.validate": true,
    "files.associations": {
        "*.yaml": "yaml"
    },
```

Save the file and reload VS Code to finish the process.

If everything worked as expected, when we create a new .yaml file and press CTRL + Space, VS Code should then display the suggestions based on the schema we created for this file type. Note that, it could take some seconds for VS Code to index the schema in the first time.


## Validation
You can also check the validity of the YAML files here by uploading or copy pasting your YAML file:
https://data.dev.catalogueoflife.org/tools/metadata-validator

## Update data in github
Send the modified latest.yaml file with the name of the alias to Markus, who will merge it into the repository again.

