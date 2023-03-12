const express = require('express');
const app = express();
const usersRouter = require('./routes/users');
const errorHandler = require('./middlewares/errorHandler');

// Middleware
app.use(express.json());

// Routes
app.use('/users', usersRouter);

// Error handling middleware
app.use(errorHandler);

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
