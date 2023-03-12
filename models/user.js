const mysql = require('mysql');
const config = require('../config');

const pool = mysql.createPool(config);

module.exports = {
  getAllUsers(callback) {
    pool.query('SELECT * FROM users', callback);
  },
  getUserById(id, callback) {
    pool.query('SELECT * FROM users WHERE id = ?', [id], callback);
  },
  createUser(user, callback) {
    pool.query('INSERT INTO users SET ?', user, callback);
  },
  updateUser(id, user, callback) {
    pool.query('UPDATE users SET ? WHERE id = ?', [user, id], callback);
  },
  deleteUser(id, callback) {
    pool.query('DELETE FROM users WHERE id = ?', [id], callback);
  }
};

