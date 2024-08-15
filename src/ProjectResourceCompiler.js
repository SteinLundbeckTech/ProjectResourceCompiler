/*
    @Author     Stein Lundbeck
    @Date       15.08.2024
    @Latest     15.08.2024
*/

const { ProcessTypes, ProcessProperties, OutputTypes, Path, Log, GetDefault, PRCUtility } = require("./PRCUtility");

let util = new PRCUtility();

let test = GetDefault(ProcessTypes.Style, ProcessProperties.BundleEnabled);

WriteLine("test");
