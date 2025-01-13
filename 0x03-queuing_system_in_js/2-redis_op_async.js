import redis from 'redis';
import { promisify } from 'util';
import { createClient } from 'redis';

const client = createClient();

// Promisify the Redis get command
const getAsync = promisify(client.get).bind(client);

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, redis.print);
};

const displaySchoolValue = async (schoolName) => {
    try {
        const value = await getAsync(schoolName);
        console.log(value);
    } catch (error) {
        console.error(error);
    }
};

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

// Using an async IIFE (Immediately Invoked Function Expression) to use await
(async () => {
    await displaySchoolValue('ALX');
    setNewSchool('ALXSanFrancisco', '100');
    await displaySchoolValue('ALXSanFrancisco');
})();