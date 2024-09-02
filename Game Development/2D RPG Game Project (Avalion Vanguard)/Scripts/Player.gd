extends CharacterBody2D

@export var SPEED = 250.0
func get_input():
	var input_direction = Input.get_vector("move_left", "move_right", "move_up", "move_down")
	velocity = input_direction * SPEED

func _physics_process(_delta):
	get_input()
	move_and_slide()

@onready var _animated_sprite = $AnimatedSprite2D
func walkingAnim_check():
	if velocity.x || velocity.y != 0:
		_animated_sprite.play("Walk")
	else:
		_animated_sprite.play("Idle")

func directionAnim_check():
	if Input.is_action_pressed("move_left"):
		_animated_sprite.flip_h = true
	elif Input.is_action_pressed("move_right"):
		_animated_sprite.flip_h = false

func _process(_delta):
	walkingAnim_check()
	directionAnim_check()
