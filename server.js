const http = require('http');
const fs = require('fs');
const path = require('path');

const port = process.env.PORT || 8080;

const mime = {
  '.html': 'text/html',
  '.css': 'text/css',
  '.js': 'application/javascript',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.webp': 'image/webp',
};

const server = http.createServer((req, res) => {
  const safePath = path.normalize(decodeURI(req.url)).replace(/^\.+/, '');
  let filePath = path.join(process.cwd(), 'dist', safePath);
  if (filePath.endsWith(path.sep) || req.url === '/' ) filePath = path.join(process.cwd(), 'dist', 'index.html');
  if (!fs.existsSync(filePath)) {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not found');
    return;
  }
  const ext = path.extname(filePath) || '.html';
  const type = mime[ext] || 'application/octet-stream';
  res.writeHead(200, { 'Content-Type': type });
  fs.createReadStream(filePath).pipe(res);
});

server.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/ (serving index_limpo.html)`);
});
