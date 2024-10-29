import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._model.build_graph()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(
            ft.Text(f"Creato grafo con {self._model.getNumNodi()} vertici e {self._model.getNumArchi()} archi"))

        self._view.txt_result.controls.append(
            ft.Text(f"Peso minimo: {self._model.get_min_weight()} Peso massimo: {self._model.get_max_weight()} "))

        self._view.update_page()

    def handle_countedges(self, e):
        valore = float(self._view.txt_name.value)
        if valore < self._model.get_min_weight() or valore > self._model.get_max_weight():
            self._view.create_alert("Valore non nella soglia calcolata")
            return
        count_bigger, count_smaller = self._model.contaValoriSoglia(valore)
        self._view.txt_result2.controls.append(ft.Text(f"Numero archi con peso maggiore della soglia: {count_bigger}"))
        self._view.txt_result2.controls.append(ft.Text(f"Numero archi con peso minore della soglia: {count_smaller}"))
        self._view.update_page()

    def handle_search(self, e):
        pass