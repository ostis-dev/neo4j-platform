const webpack = require('webpack');
const path = require('path');

const outputPath = path.resolve(__dirname, 'assets');

module.exports = {
    mode: 'none',
    entry: {
        app: './src/index.tsx'
    },
    module: {
        rules: [
            {
                test: /\.tsx?$/,
                use: 'ts-loader',
                exclude: /node_modules/
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            },
            {
                test: /\.(woff(2)?|ttf|eot|svg|png)(\?v=\d+\.\d+\.\d+)?$/,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            name: '[name].[ext]',
                            outputPath: 'fonts/'
                        }
                    }
                ]
            }
        ]
    },
    plugins: [
        new webpack.DefinePlugin({
            'process.env.NODE_ENV': JSON.stringify('production')
        }),
    ],
    resolve: {
        extensions: ['.tsx', '.ts', '.js', '.css']
    },
    externalsPresets: { node: true },
    output: {
        filename: 'sc-web.js',
        path: outputPath,
        libraryTarget: 'umd',
        library: 'ScWeb'
    }
};