from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.sweet_model import Sweet
from views import sweet_view

# Importamos el decorador de roles
from utils.decorators import role_required

sweet_bp = Blueprint("sweet", __name__)


@sweet_bp.route("/sweets")
@login_required
def list_sweets():
    sweets = Sweet.get_all()
    return sweet_view.list_sweets(sweets)


@sweet_bp.route("/sweets/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_sweet():
    if request.method == "POST":
        if current_user.has_role("admin"):
            marca = request.form["marca"]
            peso = request.form["peso"]
            sabor = request.form["sabor"]
            origen = request.form["origen"]
            sweet = Sweet(marca=marca, peso=peso, sabor=sabor, origen=origen)
            sweet.save()
            flash("sweet creado exitosamente", "success")
            return redirect(url_for("sweet.list_sweets"))
        else:
            return jsonify({"message": "Unpesoized"}), 403
    return sweet_view.create_sweet()


@sweet_bp.route("/sweets/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_sweet(id):
    sweet = Sweet.get_by_id(id)
    if not sweet:
        return "sweet no encontrado", 404
    if request.method == "POST":
        if current_user.has_role("admin"):
            marca = request.form["marca"]
            peso = request.form["peso"]
            sabor = request.form["sabor"]
            origen = bool(request.form["origen"])
            sweet.update(marca=marca, peso=peso, sabor=sabor, origen=origen)
            flash("sweet actualizado exitosamente", "success")
            return redirect(url_for("sweet.list_sweets"))
        else:
            return jsonify({"message": "Unpesoized"}), 403
    return sweet_view.update_sweet(sweet)


@sweet_bp.route("/sweets/<int:id>/delete")
@login_required
@role_required("admin")
def delete_sweet(id):
    sweet = Sweet.get_by_id(id)
    if not sweet:
        return "sweet no encontrado", 404
    if current_user.has_role("admin"):
        sweet.delete()
        flash("sweet eliminado exitosamente", "success")
        return redirect(url_for("sweet.list_sweets"))
    else:
        return jsonify({"message": "Unpesoized"}), 403