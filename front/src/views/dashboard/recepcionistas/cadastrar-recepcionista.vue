<template>
	<LayoutDashboard>
		<div class="sm:ml-[60px] mt-[29px]">
			<router-link to="/dashboard/medicos">
				<h2
					class="text-lg font-semibold text-gray-600 transition duration-300 ease-in-out hover:text-gray-800 sm:text-xl">
					Voltar</h2>
			</router-link>
		</div>

		<div class="grid grid-cols-1 gap-4 ml-[25px] sm:ml-[145px] mt-[20px]">
			<h1 class="mb-6 text-[1.75rem] font-normal sm:text-[3.125rem] sm:font-montserrat">Cadastrar Recepcionista
			</h1>
			<div class="rounded-xl sm:rounded-none pb-[70px] pt-[29px] sm:pt-[40px] px-[20px] sm:px-[60px] mb-4 bg-white ded-lgroun gap-x-4 sm:w-[650px]"
				style="box-shadow: 0px 4px 4px 0px #00000040; box-shadow: 0px 4px 4px 0px #00000040; box-shadow: 0px -2px 0px 0px #00000040;">
				<form @submit.prevent="submitForm">
					<h2 class="mb-4 text-xl font-bold text-black font-montserrat">Dados Pessoais</h2>

					<div class="grid grid-cols-1 gap-4">
						<div>
							<label class="block mb-2 text-sm sm:text-lg font-montserrat">
								Nome:
							</label>
							<input v-model="FormData.name" type="text" class="px-2 py-1 w-full rounded-2xl border" />
							<div v-if="formErrors.name" class="mt-1 text-sm text-red-500">
								{{ formErrors.name }}
							</div>
						</div>
						<div>
							<label class="block mb-2 text-sm sm:text-lg font-montserrat br-16">
								Sobrenome:
							</label>
							<input v-model="FormData.lastName" type="text"
								class="px-2 py-1 w-full rounded-2xl border" />
						</div>
						<div class="sm:flex flex-coll gap-[80px]">
							<div>
								<label class="block mb-2 text-sm sm:text-lg font-montserrat br-16">
									Data de Nascimento:
								</label>
								<input v-model="FormData.dateOfBirth" type="date"
									class="w-[164px] px-2 py-1 border rounded-2xl" />
							</div>
							<div>
								<label class="mt-[20px] sm:mt-0 block mb-2 text-sm sm:text-lg font-montserrat br-16">
									Gênero:
								</label>
								<select v-model="FormData.gener" class="w-[164px] px-2 py-1 border rounded-2xl">
									<option value="Feminino">Feminino</option>
									<option value="Masculino">Masculino</option>
								</select>
							</div>
						</div>
						<div>
							<label class="block mb-2 text-sm sm:text-lg font-montserrat br-16">
								CPF:
							</label>
							<input v-model="FormData.cpf" type="text" class="px-2 py-1 w-full rounded-2xl border"
								placeholder="999.999.999-99" />
							<div v-if="formErrors.cpf" class="mt-1 text-sm text-red-500">
								{{ formErrors.cpf }}
							</div>
						</div>
					</div>
					<h2 class="mb-4 text-xl font-montserrat text-black mt-[30px] font-bold">Endereço:</h2>
					<div class="flex gap-[40px]">
						<div>
							<label class="block mb-2 text-sm sm:text-lg font-montserrat br-16">
								País:
							</label>
							<select v-model="FormData.country" class="w-[100px] px-2 py-1 border rounded-2xl">
								<option value="brasil">Brasil</option>
								<option value="EUA">EUA</option>
							</select>
						</div>
						<div>
							<label class="block mb-2 text-sm sm:text-lg font-montserrat br-16">
								Estado:
							</label>
							<select v-model="FormData.state" class="w-[100px] px-2 py-1 border rounded-2xl">
								<option value="RN">RN</option>
								<option value="PB">PB</option>
							</select>
						</div>
					</div>
					<div class="flex-coll sm:flex gap-[10px] mt-3">
						<div>
							<label class="block mb-2 text-sm sm:text-lg font-montserrat br-16">
								Cidade:
							</label>
							<input v-model="FormData.city" type="text" class="px-2 py-1 w-full rounded-2xl border"
								placeholder="Parnamirim" />
						</div>
						<div>
							<label class=" mt-[20px] sm:mt-0 block mb-2 text-sm sm:text-lg font-montserrat br-16">
								Bairro:
							</label>
							<input v-model="FormData.neighborhood" type="text"
								class="px-2 py-1 w-full rounded-2xl border" placeholder="Nova Parnamirim" />
						</div>
					</div>
					<div>
						<label class="block mt-[20px] mb-2 text-sm sm:text-lg font-montserrat br-16">
							CEP:
						</label>
						<input v-model="FormData.zipCode" type="text" class="px-2 py-1 w-full rounded-2xl border"
							placeholder="00000-000" />
					</div>
					<div class="flex-coll sm:flex gap-[10px]">
						<div>
							<label class="block mt-[20px] mb-2 text-sm sm:text-lg font-montserrat br-16">
								Logradouro:
							</label>
							<input v-model="FormData.street" type="text"
								class="w-full sm:w-[432px] px-2 py-1 border rounded-2xl"
								placeholder="Av. Maria Lacerda Montenegro" />
						</div>
						<div>
							<label class="block mt-[20px] mb-2 text-sm sm:text-lg font-montserrat br-16">
								Número:
							</label>
							<input v-model="FormData.number" type="text" class="w-[88px] px-2 py-1 border rounded-2xl"
								placeholder="000" />
						</div>
					</div>
					<h2 class="mt-[30px] mb-4 text-xl font-montserrat text-black font-bold">Contato</h2>
					<div>
						<label class="block mt-[20px] mb-2 text-sm sm:text-lg font-montserrat br-16">
							Email:
						</label>
						<input v-model="FormData.email" type="email"
							class="w-full sm:w-[432px] px-2 py-1 border rounded-2xl"
							placeholder="exemplo99@email.com" />
						<div v-if="formErrors.email" class="mt-1 text-sm text-red-500">
							{{ formErrors.email }}
						</div>
					</div>
					<div>
						<label class="block mt-[20px] mb-2 text-sm sm:text-lg font-montserrat br-16">
							Senha:
						</label>
						<input v-model="FormData.password" type="password"
							class="w-full sm:w-[432px] px-2 py-1 border rounded-2xl" placeholder="Digite sua senha" />
						<div v-if="formErrors.password" class="mt-1 text-sm text-red-500">
							{{ formErrors.password }}
						</div>
					</div>
					<div>
						<label class="block mt-[20px] mb-2 text-sm sm:text-lg font-montserrat br-16">
							Celular:
						</label>
						<input v-model="FormData.phone" type="tel" class="w-[250px] px-2 py-1 border rounded-2xl"
							placeholder="(00) 0 0000-0000" />
					</div>
					<h2 class="mt-[30px] mb-4 text-xl font-montserrat text-black font-bold">Expediente:</h2>
					<div>
						<label class="block mt-[20px] mb-2 text-sm sm:text-lg font-montserrat br-16">
							Dias de Trabalho (Selecione os dias):
						</label>
						<DaysSelector @update:selected-days="handleSelectedDays" />
					</div>
					<div>
						<label class="block mt-[20px] mb-2 text-sm sm:text-lg font-montserrat br-16">
							Turnos:
						</label>
						<WorkShifts :selectedShifts="selectedShifts" @update:selected-shifts="handleSelectedShifts" />
					</div>
					<div class="flex flex-col">
						<label class="block mt-[20px] mb-2 text-sm sm:text-lg font-montserrat br-16">
							Disponibilidade para plantões:
						</label>
						<label class="flex gap-2 items-center cursor-pointer">
							<input type="radio" value="sim" v-model="FormData.plantoes"
								class="cursor-pointer custom-radio-square">Sim
						</label>
						<label class="flex gap-2 items-center cursor-pointer">
							<input type="radio" value="nao" v-model="FormData.plantoes"
								class="cursor-pointer custom-radio-square">Não
						</label>
					</div>

					<button class="mt-[40px] bg-[#00428F] text-white w-[104px] h-[42px] rounded-lg btn"
						@click="submitForm">Cadastrar</button>
					<dialog id="my_modal_4" class="modal" ref="modal" @click.self="closeModal">

						<div class="modal-box w-[310px] sm:w-[750px] max-w-5xl">

							<div>
								<h1 class="font-montserrat text-[1.375rem] font-semibold text-center">Recepcionista
									cadastrado com sucesso!</h1>
							</div>

							<ModalCadastro :FormData="FormData">
								<template v-slot:header>
									<h1 class="mb-6 font-bold text-[30px] w-[640px] text-h1 font-montserrat">
										Recepcionista cadastrado com sucesso!</h1>

									<h2 class="mb-4 text-xl font-bold text-black font-montserrat">Dados Pessoais:</h2>
								</template>

								<h2 class="mt-[30px] mb-4 text-xl font-montserrat text-black font-bold">Expediente:</h2>
								<span class="block mt-[20px] mb-2 text-lg font-montserrat br-16 font-semibold">
									Dias de Trabalho:
								</span>
								<div class="flex flex-wrap gap-2">
									<span v-for="(day, index) in weekDays" :key="index" :class="[
										'px-px-4 py-2 rounded-2xl cursor-pointer w-[90px] h-[30px] flex items-center justify-center font-montserrat',
										selectedDays.includes(day) ? 'bg-[#00428F] text-white' : 'bg-[#DEECFA] text-gray-700'
									]">
										{{ day }}
									</span>
								</div>
								<span class="block mt-[20px] mb-2 text-lg font-montserrat br-16 font-semibold">
									Turnos:
								</span>
								<div class="flex flex-wrap gap-2">

									<span v-for="(shift, index) in shifts" :key="index" :class="[
										'px-px-4 py-2 rounded-2xl cursor-pointer w-[90px] h-[30px] flex items-center justify-center font-montserrat',
										selectedShifts.includes(shift) ? 'bg-[#00428F] text-white' : 'bg-[#DEECFA] text-gray-700'
									]">
										{{ shift }}
									</span>
								</div>
								<span class="block mt-[20px] mb-2 text-lg font-montserrat br-16 font-semibold">
									Disponibilidade para plantões:
								</span>

								<div class="flex flex-col gap-2">
									<label class="flex gap-2 items-center">
										<input type="radio" value="sim" v-model="FormData.plantoes" disabled
											class="custom-radio-square" />
										Sim
									</label>
									<label class="flex gap-2 items-center">
										<input type="radio" value="nao" v-model="FormData.plantoes" disabled
											class="custom-radio-square" />
										Não
									</label>
								</div>
							</ModalCadastro>
							<div class="flex flex-col justify-between modal-action">

								<div class="flex w-full pl-[50px] justify-center sm:justify-start">

									<form method="dialog">
										<!-- if there is a button, it will close the modal -->
										<button @click="closeModal"
											class="bg-[#00428F] text-white w-[104px] h-[42px] rounded-lg mt-auto">Fechar</button>
									</form>
									<form method="dialog" class="modal-backdrop">
										<button>Fechar</button>
									</form>
								</div>
							</div>
						</div>
					</dialog>
				</form>
			</div>

		</div>

	</LayoutDashboard>
</template>


<script setup lang="ts">
import DaysSelector from '@/components/baseUi/DaysSelector.vue';
import ModalCadastro from '@/components/baseUi/ModalCadastro.vue';
import WorkShifts from '@/components/baseUi/WorkShifts.vue';
import LayoutDashboard from '@/layouts/LayoutDashboard.vue'
import { useUserStore } from '@/stores/users/users.store'
import { objectEntries } from '@vueuse/core';
import { reactive, ref } from 'vue';
import { toast } from 'vue-sonner';
import { useRouter } from 'vue-router';

const router = useRouter();
const userStore = useUserStore();

const weekDays = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo'];
const shifts = ['Matutino', 'Vespertino', 'Noturno']
const selectedDays = ref<string[]>([]);
const selectedShifts = ref<string[]>([]);
const formErrors = ref<Record<string, string>>({});

//lista de dias
const handleSelectedDays = (days: string[]) => {
	selectedDays.value = days;
}
//Lista de horários 
const handleSelectedShifts = (shifts: string[]) => {
	selectedShifts.value = shifts;
}

// reactive pq formData é um objeto
const FormData = reactive({
	name: '',
	lastName: '',
	dateOfBirth: '',
	gener: 'Feminino',
	cpf: '',
	country: 'Brasil',
	state: 'RN',
	city: '',
	neighborhood: '',
	zipCode: '',
	street: '',
	number: '',
	email: '',
	phone: '',
	days: '',
	shifts: '',
	plantoes: '',
	password: ''
})

//Constante para manipular modal e poder fechar ao clicar fora do modal
const modal = ref<HTMLDialogElement | null>(null);

//função para fechar ao clicar fora
const closeModal = () => {
	modal.value?.close();
	router.push('/dashboard/recepcionistas');
}

const validateForm = () => {
	const errors: Record<string, string> = {};

	if (!FormData.name.trim()) {
		errors.name = 'Nome é obrigatório';
	}

	if (!FormData.cpf.trim()) {
		errors.cpf = 'CPF é obrigatório';
	}

	if (!FormData.email.trim()) {
		errors.email = 'Email é obrigatório';
	} else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(FormData.email)) {
		errors.email = 'Email inválido';
	}

	if (!FormData.password.trim()) {
		errors.password = 'Senha é obrigatória';
	} else if (FormData.password.length < 6) {
		errors.password = 'A senha deve ter pelo menos 6 caracteres';
	}

	formErrors.value = errors;
	return Object.keys(errors).length === 0;
}

const submitForm = async () => {
	if (!validateForm()) {
		toast.error('Por favor, corrija os erros no formulário');
		return;
	}

	try {
		const receptionistData = {
			first_name: FormData.name,
			last_name: FormData.lastName,
			date_birth: FormData.dateOfBirth,
			gender: FormData.gener,
			cpf: FormData.cpf,
			address: {
				country: FormData.country,
				state: FormData.state,
				city: FormData.city,
				neighborhood: FormData.neighborhood,
				zip_code: FormData.zipCode,
				street: FormData.street,
				number: FormData.number
			},
			email: FormData.email,
			password: FormData.password,
			phone: FormData.phone,
			working_days: selectedDays.value,
			working_shifts: selectedShifts.value,
			on_call_availability: FormData.plantoes === 'sim'
		};

		await userStore.createReceptionist(receptionistData);
		toast.success('Recepcionista cadastrado com sucesso!');
		modal.value?.showModal();
	} catch (error: any) {
		if (error.message === 'dados inválidos') {
			// Handle validation errors from the API
			const apiErrors = userStore.validationErrors;
			// Update form errors with API validation messages
			formErrors.value = Object.keys(apiErrors).reduce((acc, key) => {
				acc[key] = apiErrors[key][0];
				return acc;
			}, {} as Record<string, string>);
			toast.error('Por favor, corrija os erros no formulário');
		} else {
			toast.error('Erro ao cadastrar recepcionista');
		}
	}
};

</script>


<style scoped>
.custom-radio-square {
	/* Oculta o círculo padrão */
	appearance: none;
	-webkit-appearance: none;
	-moz-appearance: none;

	/* Estilos para o quadrado */
	width: 1rem;
	/* Tamanho do quadrado */
	height: 1rem;
	border: 2px solid #00428F;
	/* Bordas do quadrado */
	background-color: transparent;
	border-radius: 4px;
	/* Para manter o quadrado */

	/* Efeito ao ser selecionado */
	display: flex;
	align-items: center;
	justify-content: center;
}

.custom-radio-square:checked {
	background-color: #00428F;
	/* Cor de fundo quando selecionado */
	border-color: #00428F;
	/* Cor da borda quando selecionado */
}

h1,
h2,
p,
span,
label {
	font-family: 'montserrat';
}

label {
	color: #010424;
}
</style>