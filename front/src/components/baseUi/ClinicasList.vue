<template>
	<div class="overflow-hidden bg-white rounded-3xl shadow-lg">
		<div class="flex justify-between items-center p-4 text-white bg-primary">
			<h2 class="text-xl font-semibold">CLÍNICAS</h2>
			<button @click="navigateToAddClinic"
				class="px-4 py-2 text-blue-600 bg-white rounded-md transition-colors hover:bg-blue-100">
				Adicionar
			</button>
		</div>
		<ul>
			<li v-for="clinica in clinicas" :key="clinica.uuid" class="border-b last:border-b-0">
				<div class="flex justify-between items-center p-4 hover:bg-blue-200">
					<span>{{ clinica.name }}</span>
					<div class="max-lg:flex max-lg:flex-col max-lg:space-y-1">
						<button @click="editClinica(clinica.id)"
							class="px-3 py-1 mr-2 text-white bg-blue-600 rounded-md transition-colors hover:bg-blue-600 max-lg:w-full">
							Editar
						</button>
						<button @click="deleteClinica(clinica.id)"
							class="px-3 py-1 text-white bg-red-500 rounded-md transition-colors hover:bg-red-600">
							Excluir
						</button>
					</div>
				</div>
			</li>
		</ul>

		<dialog ref="modalDelete" id="exclusao" class="modal">
			<div class="modal-box">
				<h3 class="text-xl font-bold text-center">Tem certeza que deseja excluir?</h3>
				<div class="flex gap-4 justify-center mt-4">
					<button @click="closeModalDelete" class="text-black bg-gray-300 btn">
						Cancelar
					</button>
					<button @click="confirmActionDelete" class="text-white btn bg-primary">
						Confirmar
					</button>
				</div>
			</div>
			<form method="dialog" class="modal-backdrop">
				<button>Fechar</button>
			</form>
		</dialog>
	</div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import type { Clinic } from '@/types/clinic.types'
import { clinicService } from '@/services/clinic.service'
import { toast } from 'vue-sonner'

const clinicaParaExcluir = ref<Clinic | null>(null)

const clinicas = ref<Clinic[]>([])

onMounted(async () => {
	try {
		const response = await clinicService.getAllClinics()
		console.log('Clinicas:', response)
		clinicas.value = response ?? []
	} catch (error) {
		console.error('Erro ao buscar clinicas', error)
	}
})


const router = useRouter()
const modalEdit = ref<HTMLDialogElement>()
const modalDelete = ref<HTMLDialogElement>()


const closeModalDelete = () => {
	modalDelete.value?.close()
}

const showModalDelete = () => {
	modalDelete.value?.showModal()
}

const navigateToAddClinic = () => {
	router.push('/dashboard/clinicas/cadastrar/')
}

const editClinica = (id: number) => {
	console.log('Editar clinica')
	router.push(`/dashboard/clinicas/cadastrar/${id}`)
}

const deleteClinica = (id: number) => {
	console.log('Delete clinica', id)
	const clinicaToDelete = clinicas.value.find((c) => c.id === id)
	if (clinicaToDelete) {
		clinicaParaExcluir.value = clinicaToDelete
		showModalDelete()
	}
	showModalDelete()
}

const confirmActionDelete =async () => {
	console.log('deleted')
	if(clinicaParaExcluir.value){
		try{
			await clinicService.deleteClinic(clinicaParaExcluir.value.id)
			clinicas.value = clinicas.value.filter((c) => c.id !== clinicaParaExcluir.value?.id)
			closeModalDelete()
		}catch(error){
			toast.error('Erro ao excluir clinica')
		}
	}
}
</script>

<style scoped>
ul {
	list-style: none;
	padding: 0;
}

ul li:nth-child(even) {
	background-color: #deecfa;
}
</style>
