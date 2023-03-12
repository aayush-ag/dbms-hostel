const userModel = require('../models/user');

// GET /users
async function getAllUsers(req, res, next) {
  try {
    const users = await userModel.getAllUsers();
    res.json(users);
  } catch (err) {
    next(err);
  }
}

// GET /users/:id
async function getUserById(req, res, next) {
  try {
    const user = await userModel.getUserById(req.params.id);
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }
    res.json(user);
  } catch (err) {
    next(err);
  }
}

// POST /users
async function createUser(req, res, next) {
  try {
    const result = await userModel.createUser(req.body);
    const createdUser = { ...req.body, id: result.insertId };
    res.status(201).json(createdUser);
  } catch (err) {
    next(err);
  }
}

// PUT /users/:id
async function updateUser(req, res, next) {
  try {
    const user = await userModel.getUserById(req.params.id);
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }
    const result = await userModel.updateUser(req.params.id, req.body);
    const updatedUser = { ...user, ...req.body };
    res.json(updatedUser);
  } catch (err) {
    next(err);
  }
}

// DELETE /users/:id
async function deleteUser(req, res, next) {
  try {
    const user = await userModel.getUserById(req.params.id);
    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }
    await userModel.deleteUser(req.params.id);
    res.sendStatus(204);
  } catch (err) {
    next(err);
  }
}

module.exports = {
  getAllUsers,
  getUserById,
  createUser,
  updateUser,
  deleteUser
};
