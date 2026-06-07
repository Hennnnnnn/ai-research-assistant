export interface ResearchData {
    overview: string;
    key_findings: CitationItem[];
    risks: CitationItem[];
    future_trends: CitationItem[];
    sources: SourceItem[];
}

export interface SourceItem {
    id: number;
    title: string;
    url: string;
}

export interface Research {
    id: number;
    topic: string;
    research_data: ResearchData;
    status: string;
    created_at: string;
}

export interface ResearchListItem {
    id: number;
    topic: string;
    created_at: string;
    status: string;
}

export interface PaginatedResearchResponse {
    items: Research[];
    total: number;
    page: number;
    page_size: number;
}

export interface CitationItem {
    statement: string;
    source_id: number;
}