import redis from 'redis';
import { createClient } from 'redis';

const client = createClient();

// Connect to Redis
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

// Store hash values
function setHashFields() {
    client.hset('ALX', 'Portland', '50', redis.print);
    client.hset('ALX', 'Seattle', '80', redis.print);
    client.hset('ALX', 'New York', '20', redis.print);
    client.hset('ALX', 'Bogota', '20', redis.print);
    client.hset('ALX', 'Cali', '40', redis.print);
    client.hset('ALX', 'Paris', '2', redis.print);
}

// Display hash values
function displayHash() {
    client.hgetall('ALX', (err, result) => {
        if (err) {
            console.error(err);
            return;
        }
        console.log(result);
    });
}

// Execute operations
setHashFields();
displayHash();