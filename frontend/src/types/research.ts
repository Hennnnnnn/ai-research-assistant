export interface ResearchData {
    overview: string;
    key_findings: string[];
    risks: string[];
    future_trends: string[];
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
    created_at: string;
}

export interface PaginatedResearchResponse {
    items: Research[];
    total: number;
    page: number;
    page_size: number;
}