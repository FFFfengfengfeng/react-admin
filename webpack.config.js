/**
 * webpack配置文件
 * __dirname是node中的一个全局变量,指向执行脚本所在的目录
 * webpack.config.js配置好之后只需要在命令行运行webpack
 */
const webpack = require('webpack');
const htmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    devtool: 'eval-source-map',
    entry: __dirname + '/app/main.js',//入口文件
    output: {

        path: __dirname + '/build',//输出目录
        filename: 'bundle-[hash].js'//输出文件名
    },
    devServer: {
        contentBase: './public',//本地服务器加载的页面所在的目录
        historyApiFallback: true, //不跳转
        inline: true,//实时刷新
        hot: true
    },
    plugins: [
        new webpack.BannerPlugin('版权所有,翻版必究'),
        new htmlWebpackPlugin({
            template: __dirname + '/app/index.tmpl.html'
        }),
        new webpack.HotModuleReplacementPlugin(),
        new webpack.optimize.UglifyJsPlugin(),
    ],
    module: {
        rules: [
            {
                test: /(\.jsx|.\js)$/,
                use: {
                    loader: 'babel-loader'
                },
                exclude: /node_modules/
            },
            {
                test: /\.css$/,
                use: [
                    {
                        loader: 'style-loader'
                    },
                    {
                        loader: 'css-loader',
                        options: {
                            modules: true
                        }
                    }
                ]
            },
            {
                test: /\.less$/,
                use: [
                    {
                        loader: 'style-loader'
                    },
                    {
                        loader: 'css-loader'
                    },
                    {
                        loader: 'less-loader'
                    }
                ]
            }
        ]
    }
}