/*
    @Author     Stein Lundbeck
    @Date       15.08.2024
    @Latest     15.08.2024
*/

const { ProcessTypes, ProcessProperties, LogTypes, Logger, PRCUtility } = require("./PRCUtility");
const fs = require("fs");

let utility = new PRCUtility();

utility.Log("Loading Project Resource Compiler / Project count " + utility.Config.ProjectsJSON.length);

