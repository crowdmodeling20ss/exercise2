# Exercise-2 Vadere
add desc

## Vadere Project Configuration
Give absolte path for the vadere project before launching vadere application to prevent errors. Open **~/.config/vadere.conf** and give an absolute path following attributes:

```
History.lastUsedProject =ABSOLUTE_PATH/vadere.project
History.recentProjects =ABSOLUTE_PATH/vadere.project
ProjectView.defaultDirectory = ABSOLUTE_PATH
SettingsDialog.snapshotDirectory.path = ABSOLUTE_PATH
```

Example ABSOLUTE_PATH:

```
/Users/farukcankaya/Praktikum/exercise2
```

## Output Files
"output" directory which is automatically generated when a vadere scenario is run is ignored by default. Since a lot of tests will be needed to find a correct scenario setting, there will be huge amount of output files. Most probably, we will push all output files which also contain wrong data when a task is completed. To prevent it, output directory is ignored.

**If you want to keep output file in remote, put then into /output-remote directory.**