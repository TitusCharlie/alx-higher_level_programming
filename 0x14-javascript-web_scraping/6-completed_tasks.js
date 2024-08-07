#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
    console.log('Usage: ./6-completed_tasks.js <API URL>');
    process.exit(1);
}

const apiUrl = process.argv[2];

request.get(apiUrl, { json: true }, (error, response, body) => {
    if (error) {
        console.error('Error:', error);
        return;
    }

    const tasksCompleted = {};

    body.forEach((task) => {
        if (task.completed) {
            if (tasksCompleted[task.userId]) {
                tasksCompleted[task.userId] += 1;
            } else {
                tasksCompleted[task.userId] = 1;
            }
        }
    });

    console.log(tasksCompleted);
});