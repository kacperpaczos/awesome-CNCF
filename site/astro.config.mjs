// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { sidebar } from './starlight.sidebar.mjs';

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'CNCF Cloud Native KB',
			description:
				'Baza wiedzy o projektach CNCF Landscape — use cases, alternatywy, OpenAPI.',
			logo: {
				src: './src/assets/logo.svg',
				replacesTitle: false,
			},
			social: [
				{
					icon: 'github',
					label: 'GitHub',
					href: 'https://github.com/cncf/landscape-2',
				},
				{
					icon: 'external',
					label: 'CNCF Landscape',
					href: 'https://landscape.cncf.io',
				},
			],
			sidebar,
			customCss: ['./src/styles/custom.css'],
		}),
	],
});
