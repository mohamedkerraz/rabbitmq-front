const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:3000/',
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
      },
      '/consumer/socket.io': {
        target: 'http://127.0.0.1:5000',
        ws: true,
        changeOrigin: true
      }
    }
  }
});
