import { createQueue } from 'kue';

const queue = createQueue();

const notif = {
  phoneNumber: '666666666',
  message: 'this is how you can contact him'
};

const job = queue.create('push_notification_code', notif).save(err => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
});
