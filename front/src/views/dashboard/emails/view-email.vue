<template>
    <LayoutDashboard>
        <div class="p-8">
            <h1 class="text-4xl font-bold">{{ emailInfo.nome }}</h1>
            <p class="mb-6 text-xl">Recebido dia {{ formatDate(emailInfo.respondido_data) }}</p>

            <div class="min-h-[60vh] p-6 mb-4 bg-white rounded-lg shadow-lg">
                <div class="flex flex-col mb-6 gap-y-4">
                    <!-- email, subject, telefone, message -->
                    <div class="flex items-center gap-x-2">
                        <p class="text-xl font-bold">Email:</p>
                        <p class="text-md">{{ emailInfo.email }}</p>
                    </div>

                    <div class="flex items-center gap-x-2">
                        <p class="text-xl font-bold">Assunto:</p>
                        <p class="text-md">{{ emailInfo.assunto }}</p>
                         <!-- <p>Assunto</p> -->
                    </div>

                    <div class="flex items-center gap-x-2">
                        <p class="text-xl font-bold">Telefone:</p>
                        <p class="text-md">{{ emailInfo.telefone }}</p>
                    </div>

                    <div class="flex items-center gap-x-2">
                        <p class="text-xl font-bold">Mensagem:</p>
                        <p class="text-md">{{ emailInfo.mensagem }}</p>
                    </div>
                </div>
            </div>
            <button class="bg-[#41A9D8] text-white px-4 py-2 rounded-md" @click="repondToEmail">
                Email Respondido
            </button>
        </div>
    </LayoutDashboard>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { useRoute } from 'vue-router'
import type { Contato } from '@/types/institucional.types'
import { contatoService } from '@/services/contato.service'
import { useContatoStore } from '@/stores/contato/contato.store'
import { toast } from 'vue-sonner'

const route = useRoute()
const emailId = route.params.id
const contatoStore = useContatoStore()

function formatDate(data: string): string{
    if(!data) return '';
    const date = new Date(data);
    return isNaN(date.getTime())?'': date.toLocaleDateString('pt-BR')
}

const emailInfo = reactive<Contato>({
    id:'',
    nome:'',
    email:'',
    telefone:'',
    assunto:'',
    mensagem:'',
    respondido: false,
    respondido_data:'',
    envio_data: ''
})

onMounted(async () =>{
    try{
        if(emailId){
            const contato = await contatoService.getContato(emailId as string)
            Object.assign(emailInfo, contato)
        }
    }catch (error){
        console.error("Erro ao buscar dados", error)
    }
})



const repondToEmail = async () =>{

    try{

        const respostaData = new Date().toISOString()

        const updateContato = {
            ...emailInfo,
            respondido: true,
            respondido_data: new Date().toISOString().split('T')[0]
        }
        
        await contatoStore.updateContato(emailInfo.id, updateContato)

        toast.success('Email respondido com sucesso!')

        emailInfo.respondido = true
        emailInfo.respondido_data = respostaData
        
        
    } catch(err){
        console.error('Erro ao responder email', err)
        toast.error('Ocorreu um erro ao responder o email.')
    }
        
}

</script>
