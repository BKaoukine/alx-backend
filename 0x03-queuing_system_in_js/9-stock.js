import { createClient } from 'redis';
import { promisify } from 'util';
const express = require('express');

const client = createClient();
client.on('connect', () => console.log('Connected successfully'))
  .on('error', e => console.log(`Failed to connect: ${e}`));

const get = promisify(client.get).bind(client);

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

function getItemById (id) {
  return listProducts.filter((product) => (product.Id === id)[0]);
}

function reserveStockById (itemId, stock) {
  client.set(itemId, stock);
}

async function getCurrentReservedStockById (itemId) {
  return await get(itemId);
}

const app = express();
const port = 1245;

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(parseInt(itemId));
  if (item) {
    const stock = await getCurrentReservedStockById(itemId);
    const resItem = {
      itemId: item.itemId,
      itemName: item.itemName,
      price: item.price,
      initialAvailableQuantity: item.initialAvailableQuantity,
      currentQuantity: stock !== null ? parseInt(stock) : item.initialAvailableQuantity
    };
    res.json(resItem);
  } else {
    res.json({ status: 'Product not found' });
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(parseInt(itemId));
  if (item) {
    const stock = await getCurrentReservedStockById(itemId);
    if (stock !== null) {
      crnt_stock = parseInt(stock);
      if (crnt_stock > 0) {
        reserveStockById(itemId, crnt_stock - 1);
        res.json({ status: 'Reservation confirmed', itemId });
      } else {
        res.json({ status: 'Not enough stock available', itemId });
      }
    } else {
      reserveStockById(itemId, item.initialAvailableQuantity - 1);
      res.json({ status: 'Reservation confirmed', itemId });
    }
  } else {
    res.json({ status: 'Product not found' });
  }
});

app.listen(port);
