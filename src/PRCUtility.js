/*
    @Author         : Stein Lundbeck
    @Date           : 15.08.2024
    @Latest         : 15.08.2024
*/

const fs = require("fs");
const config = JSON.parse(fs.readFileSync(".//ProjectResourceCompilerConfig.json"));

const ProcessTypes = {
    Style: "STYLE",
    Script: "SCRIPT",
    Image: "IMAGE",
    Distro: "DISTRO"
};

const ProcessProperties = {
    Enabled: "ENABLED",
    Append: "APPEND",
    ReCompile: "RECOMPILE",
    TargetEnabled: "TARGETENABLED",
    TargetRecursive: "TARGETRECURSIVE",
    TargetMinSuffix: "TARGETMINSUFFIX",
    OutTargetEnabled: "OUTTARGETENABLED",
    BundleEnabled: "BUNDLEENABLED",
    BundleMinSuffix: "BUNDLEMINSUFFIX",
    BundleTargetEnabled: "BUNDLETARGETENABLED",
    IgnoreEnabled: "IGNOREENABLED",
    IgnoreUnderscore: "IGNOREUNDERSCORE",
    IgnoreTargetEnabled: "IGNORETARGETENABLED"
};

const OutputTypes = {
    Info: "INFO",
    Error: "ERROR"
};

const Log = (content, type = OutputTypes.Info) => {
    console.log(content);
};

const GetDefault = (type, name) => {
    let result = null;

    if (type === null) {
        switch(name.toUpperCase()) {
            case ProcessProperties.Enabled:
                result = config.default.enabled;
                break;

            case ProcessProperties.Append:
                result = config.default.append;
                break;
        }
    }
    else {
        for(let action of config.default.projects[0].actions) {
            if (action.type.toUpperCase() === type.toUpperCase()) {
                switch(name.toUpperCase()) {
                    case ProcessProperties.Enabled:
                        result = action.enabled;
                        break;

                    case ProcessProperties.ReCompile:
                        result = action.reCompile;
                        break;

                    case ProcessProperties.TargetEnabled:
                        result = action.targets[0].enabled;
                        break;

                    case ProcessProperties.TargetRecursive:
                        result = action.targets[0].recursive;
                        break;

                    case ProcessProperties.TargetMinSuffix:
                        result = action.targets[0].minSuffix;
                        break;

                    case ProcessProperties.OutTargetEnabled:
                        result = action.targets[0].out.targets[0].enabled;
                        break;

                    case ProcessProperties.BundleEnabled:
                        result = action.targets[0].bundle.enabled;
                        break;

                    case ProcessProperties.BundleMinSuffix:
                        result = action.targets[0].bundle.minSuffix;
                        break;

                    case ProcessProperties.BundleTargetEnabled:
                        result = action.targets[0].bundle.targets[0].enabled;
                        break;

                    case ProcessProperties.IgnoreEnabled:
                        result = action.targets[0].ignore.enabled;
                        break;

                    case ProcessProperties.IgnoreUnderscore:
                        result = action.targets[0].ignore.underscore;
                        break;

                    case ProcessProperties.IgnoreTargetEnabled:
                        result = action.targets[0].ignore.targets[0].enabled;
                        break;
                }
            }
        }
    }

    return result;
}

class Path {
    constructor(path) {
        this.Value = path;
    }

    IsFile() {
        return fs.statSync(this.Value).isFile();
    }

    Exists() {
        try {
            return fs.existsSync(this.Value);
        }
        catch(error) {
            Log("Error occured", OutputTypes.Error);
        }
    }
}

class Config {
    constructor() {
        this.DefaultJSON = config.default;
        this.ProjectsJSON = config.projects;
        this.Enabled = config.enabled === undefined ? GetDefault(null, ProcessProperties.Enabled) : config.enabled;
        this.Append = config.append === undefined ? GetDefault(null, ProcessProperties.Append) : config.append;
    }
}

class PRCUtility {
    constructor() {
        this.Config = new Config();
    }
}

module.exports = {
    ProcessTypes,
    ProcessProperties,
    OutputTypes,
    Log,
    GetDefault,
    Path,
    PRCUtility
};
