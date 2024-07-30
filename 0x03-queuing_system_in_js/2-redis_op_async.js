import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient()
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', e => console.log(`Redis client not connected to the server: ${e}`));

function setNewSchool (schoolName, value) {
  client.set(schoolName, value, print);
}

const get = promisify(client.get).bind(client);

async function displaySchoolValue (schoolName) {
  const result = await get(schoolName).catch(err => {
    if (err) {
      console.log(err);
      throw (err);
    }
  });
  console.log(result);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
