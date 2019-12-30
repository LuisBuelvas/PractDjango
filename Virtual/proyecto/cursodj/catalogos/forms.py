from django import forms

from catalogos.models import Categoria, SubCategoria, Producto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields = ['descripcion', 'activo']
        labels= {'descripcion': "Descripción de la Categoría",
                "activo:":"Estado"}
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class SubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset = Categoria.objects.filter(activo=True).
        order_by('descripcion')
    ) 
    class Meta:
        model=SubCategoria
        fields = ['categoria', 'descripcion', 'activo']
        labels= {
                'categoria': 'Categoria',
                'descripcion': "Descripción de la Sub-Categoría",
                "activo:":"Estado"}
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['categoria'].empty_label="Selecciones Categoria"
    
class ProductoForm(forms.ModelForm):
    subcategoria = forms.ModelChoiceField(
        queryset = SubCategoria.objects.filter(activo=True).
        order_by('categoria__descripcion', 'descripcion'),
        empty_label='Selecciones Sub-Categoria'
    )
    
    class Meta:
        model = Producto 
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        