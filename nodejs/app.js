const express = require('express');
const app = express();
const port = 3000;

app.use((req, res, next) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
  next();
});

app.get('/', (req, res) => {
  res.send('Сервер запущен');
});

app.get('/api/recipes', (req, res) => {
  res.json({
    salad: "some text",
    steak: "another text",
    soup: "one more text"
  });
});

app.get('/api/chefs', (req, res) => {
  res.json({
    chef1: "Viktor Barinov",
    chef2: "Elena Sokolova",
    chef3: "Maxim Lavrov"
  });
});

app.get('/api/recipes/:id', (req, res) => {
  res.json({
    message: "Рецепт",
    recipeId: req.params.id
  });
});

app.use((req, res) => {
  res.status(404).json({ error: 'Not Found' });
});

app.listen(port, () => {
  console.log(`Сервер запущен на http://localhost:${port}`);
});
