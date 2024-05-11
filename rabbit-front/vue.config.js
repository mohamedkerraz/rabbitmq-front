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
      }
    }
  },
  configureWebpack: {
    resolve: {
      fallback: {
        assert: require.resolve("assert/"),
        util: require.resolve("util/"),
        querystring: require.resolve("querystring-es3"),
        net: require.resolve("net-browserify"),
        tls: require.resolve("tls"),
        stream: require.resolve("stream-browserify")
      }
    }
  }
});


