import { defineConfig } from 'vite';
import MarkdownItContainer from 'markdown-it-container';
import { full as emoji } from 'markdown-it-emoji';

export default defineConfig({

   slidev: {
    vue: {
      /* vue options */
    },
    markdown: {
    markdownItSetup(md) {
      /* custom markdown-it plugins */
      md.use(require ('markdown-it-container'), 'info');
      md.use(require ('markdown-it-container'), 'warning');
      md.use(require ('markdown-it-container'), 'note');
      md.use(emoji);
  },
},
    
} 
  })

