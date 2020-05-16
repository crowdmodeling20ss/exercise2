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

## Version History
For a new implemented feature, export runnable jar files and add a new release to <a href="https://github.com/crowdmodeling20ss/vadere/releases">here</a>. In this way, we can test different features/versions quickly without building vadere again and again.
### Release Structure
- Use semantic versioning. 
- Add description for added or removed features. 
- Export vadere-postvis, vadere-gui and vadere-console jars.
- Add `-version-commithash.jar` suffix to these jar. e.g.: 
   - version: `v1.0.0`
   - commithash: `0a91c075f27987a8266cdd4ede24952346df21dc`
   - Fullname for vadere-gui: `vadere-gui-v0.0.10-0a91c075f27987a8266cdd4ede24952346df21dc.jar`

## Output Files
"output" directory which is automatically generated when a vadere scenario is run is ignored by default. Since a lot of tests will be needed to find a correct scenario setting, there will be huge amount of output files. Most probably, we will push all output files which also contain wrong data when a task is completed. To prevent it, output directory is ignored.

**If you want to keep output file in remote, put then into /output-remote directory.**
