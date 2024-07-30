function createPushNotificationsJobs (jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw Erro('Jobs is not an array');
  }
  jobs.forEach((j) => {
    const job = queue.create('push_notification_code_3', j).save(e => {
      if (!e) {
        console.log(`Notification job created: ${job.id}`);
      }
    });
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    }).on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    }).on('progress', (progress, data) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}

module.exports = createPushNotificationsJobs;
