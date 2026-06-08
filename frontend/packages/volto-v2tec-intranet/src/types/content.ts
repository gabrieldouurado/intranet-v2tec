import type { Content, RelatedItem } from '@plone/types';

export interface Area extends Content {
  title: string;
  description: string;
  telefone?: string;
  email: string;
  endereco?: string;
  complemento?: string;
  cidade?: string;
  estado?: {
    token: string;
    title?: string;
  };
  cep?: string;
}

export interface Pessoa extends Content {
  title: string;
  description: string;
  area?: RelatedItem;
  categoria?: {
    token: string;
    title: string;
  };
  telefone?: string;
  email?: string;
  endereco?: string;
  complemento?: string;
  cidade?: string;
  estado?: {
    token: string;
    title: string;
  };
  cep?: string;
}
