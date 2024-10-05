import {defineConfig, loadConfigFromFile} from 'vite';

import path from "path"

export default defineConfig({
    resolve: {
        
    },
    build: {
        rollupOptions: {
            output: {
                assetFileNames: "[hash].[ext]"
            }
        }
    }
})