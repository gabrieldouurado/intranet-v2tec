import type { ConfigType } from '@plone/registry';
import installSettings from './config/settings';
import installViews from './config/views';
import installBlocks from './config/blocks';

function applyConfig(config: ConfigType) {
  installSettings(config);
  installBlocks(config);
  installViews(config);
  return config;
}

export default applyConfig;
