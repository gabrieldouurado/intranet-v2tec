import type { ConfigType } from '@plone/registry';
import AreaGridItem from 'volto-v2tec-intranet/components/Blocks/Grid/AreaGridItem';

export default function install(config: ConfigType) {
  // Registra Componente para exibir uma Área quando a listagem for de Grade
  config.registerComponent({
    name: 'GridListingItemTemplate',
    component: AreaGridItem,
    dependencies: 'Area',
  });
  return config;
}
