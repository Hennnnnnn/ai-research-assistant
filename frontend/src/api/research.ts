import client from "./client"

export interface CreateResearchRequest {
    topic: string;
}

export async function createResearch(
    data: CreateResearchRequest
) {
    const response = await client.post(
        "/research",
        data
    )

    return response.data
}

export async function getResearchList() {
    const response = await client.get(
        "/research"
    )

    return response.data
}

export async function getResearchDetail(
    id: number
) {
    const response = await client.get(
        `/research/${id}`
    )

    return response.data
}

export async function deleteResearch(
    id: number
) {
    const response =
        await client.delete(
            `/research/${id}`
        );

    return response.data;
}

export async function exportResearchPDF(id: number) {
    return await client.get(
        `/research/${id}/pdf`,
        {
            responseType: "blob"
        }
    );
}