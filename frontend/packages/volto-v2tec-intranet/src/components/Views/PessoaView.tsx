import React from 'react';
import Image from '@plone/volto/components/theme/Image/Image';
import { Container } from '@plone/components';
import ContactInfo from 'volto-v2tec-intranet/components/ContactInfo/ContactInfo';
import AddressInfo from 'volto-v2tec-intranet/components/AddressInfo/AddressInfo';
import type { Pessoa } from 'volto-v2tec-intranet/types/content';
import UniversalLink from '@plone/volto/components/manage/UniversalLink/UniversalLink';

interface PessoaViewProps {
  content: Pessoa;
  [key: string]: any;
}

const PessoaView: React.FC<PessoaViewProps> = (props) => {
  const { content } = props;

  return (
    <Container id="page-document" className="view-wrapper pessoa-view">
      {content.image && (
        <Image
          className="documentImage ui right floated image"
          alt={content.title}
          title={content.title}
          item={content}
          imageField="image"
          responsive={true}
        />
      )}
      {content.categoria && (
        <span className={`categoria categoria-${content.categoria.token}`}>
          {content.categoria.title}
        </span>
      )}
      <h1 className="documentFirstHeading">{content.title}</h1>
      {content.description && (
        <p className="documentDescription">{content.description}</p>
      )}
      {content.area && (
        <Container className="area-container">
          <UniversalLink className={'area'} item={content.area}>
            {content.area.title}
          </UniversalLink>
        </Container>
      )}
      <ContactInfo content={content} />
      <AddressInfo content={content} />
    </Container>
  );
};

export default PessoaView;
