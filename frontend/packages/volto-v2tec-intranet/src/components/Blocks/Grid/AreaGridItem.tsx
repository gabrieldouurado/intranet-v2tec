import React from 'react';
import AreaInfo from 'volto-v2tec-intranet/components/AreaInfo/AreaInfo';
import UniversalLink from '@plone/volto/components/manage/UniversalLink/UniversalLink';
import type { RelatedItem } from '@plone/types';

interface AreaGridItemProps {
  item: RelatedItem;
}

const AreaGridItem: React.FC<AreaGridItemProps> = (props) => {
  const { item } = props;
  return (
    <div className={`card-summary`}>
      <UniversalLink className={'area'} item={item}>
        <AreaInfo content={item} icon />
      </UniversalLink>
    </div>
  );
};

export default AreaGridItem;
