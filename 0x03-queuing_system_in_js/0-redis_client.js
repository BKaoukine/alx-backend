import { createClient } from 'redis';

createClient()
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', e => console.log(`Redis client not connected to the server: ${e}`));
