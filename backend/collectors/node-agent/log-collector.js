const fs = require('fs');
const path = require('path');

// Load configuration
const configPath = path.join(__dirname, 'config.json');
const config = JSON.parse(fs.readFileSync(configPath, 'utf8'));

const logLevels = config.log_levels || ['INFO', 'WARNING', 'ERROR'];
const sources = config.sources || ['service1', 'service2', 'service3'];
const interval = config.interval_seconds || 5;

function generateLog() {
    const log = {
        timestamp: new Date().toISOString(),
        level: logLevels[Math.floor(Math.random() * logLevels.length)],
        message: `Sample log message ${Math.floor(Math.random() * 100)}`,
        source: sources[Math.floor(Math.random() * sources.length)]
    };
    return log;
}

function main() {
    setInterval(() => {
        const log = generateLog();
        console.log(JSON.stringify(log));
    }, interval * 1000);
}

main();
