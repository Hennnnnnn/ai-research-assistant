export interface ResearchData {
    overview: string;
    key_findings: string[];
    risks: string[];
    future_trends: string[];
    sources: Source[];
}

export interface Source {
    title: string;
    url: string;
}

export interface Research {
    id: number;
    topic: string;
    research_data: ResearchData;
    created_at: string;
}

export interface ResearchListItem {
    id: number;
    topic: string;
    status: string;
    created_at: string;
}

export interface PaginatedResearchResponse {
    items: Research[];
    total: number;
    page: number;
    page_size: number;
}