from OpenGL.GL import *
from glew_wish import *
import glfw
import random

def main():
    if not glfw.init():
        return
    
    window = glfw.create_window( 800, 600, "Mi ventana", None, None)

    #CONFIGURACION OPENGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #VALIDAMOS QUE SE CREE VENTANA
    if not window:
        glfw.terminate()
        return
    
   #ESTABLECEMOS EL CONTEXTO, CREAMOS LA VENTANA PERO AUN NO SE MUESTRA
    glfw.make_context_current(window)

    #aCTIVAMOS LA VALIDACION DE FUNCIONES MODERNAS DE OPENLGL

    glewExperimental = True 

    #inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #versiones de OPENGL Y SHADERS
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):

        color1= random.random()
        color2= random.random()
        color3= random.random()

        
        glViewport(0,0,800,600) #window size
        
        glClearColor(color1,color2,color3,1) #colores rgb
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #el dibujo

        
        glfw.poll_events()
        
        glfw.swap_buffers(window)

    
    glfw.destroy_window(window)
   
    glfw.terminate()

if __name__ == "__main__":
    main()


