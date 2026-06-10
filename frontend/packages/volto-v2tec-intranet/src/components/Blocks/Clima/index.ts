import ClimaBlockView from 'volto-v2tec-intranet/components/Blocks/Clima/View';
import ClimaBlockEdit from 'volto-v2tec-intranet/components/Blocks/Clima/Edit';
import { ClimaSchema } from 'volto-v2tec-intranet/components/Blocks/Clima/schema';
import ClimaSVG from '@plone/volto/icons/cloud.svg';
import type { BlockConfigBase } from '@plone/types';

export interface ClimaBlockData {
  location?: string;
  measure?: string;
}
const ClimaBlockInfo: BlockConfigBase = {
  id: 'climaBlock',
  title: 'Previsão do tempo',
  icon: ClimaSVG,
  group: 'common',
  view: ClimaBlockView,
  edit: ClimaBlockEdit,
  blockSchema: ClimaSchema,
  restricted: false,
  mostUsed: true,
  sidebarTab: 1,
  blockHasOwnFocusManagement: false,
};

export default ClimaBlockInfo;
