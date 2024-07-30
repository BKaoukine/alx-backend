function task_printer(num) {
  console.log(`########## ${num} ##########`);
}

task_printer(0);
task_printer(1);
task_printer(2);
task_printer(3);
task_printer(4);
task_printer(5);
task_printer(6);
task_printer(7);
task_printer(8);
task_printer(9);
task_printer(10);
import kue from 'kue';

import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

const list = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  }
];
createPushNotificationsJobs(list, queue);
task_printer(11);
task_printer(12);
task_printer(13);
