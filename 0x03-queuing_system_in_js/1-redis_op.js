import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

await client.connect();
console.log('Redis client connected to the server');

const setNewSchool = async (schoolName, value) => {
  await client.set(schoolName, value);
  console.log('OK');
};

const displaySchoolValue = async (schoolName) => {
  await client.get(schoolName);
  console.log(schoolName)
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
