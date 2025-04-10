import type { Address } from './clinic.types'

export interface Role {
    name: string
}

export interface User {
    id: number
    first_name: string
    email: string
    cpf: string
    date_birth: string
    roles: Role[]
    address: Address
    clinics: any[] // Update this type when clinic structure is known
    gender: string
    formacao: string
    crm: string
    attach_document: string | null
    password?: string
}
