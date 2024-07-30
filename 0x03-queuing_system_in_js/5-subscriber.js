import { createClient, print } from 'redis';

const client = createClient()
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', e => console.log(`Redis client not connected to the server: ${e}`));

client.subscribe('holberton school channel');

client.on('message', (chan, msg) => {
  console.log(msg);

  if (msg === 'KILL_SERVER') {
    client.unsubscribe('holberton school channel');
    client.end(true);
  }
});
