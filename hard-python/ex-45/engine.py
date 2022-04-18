class Engine:
    
    def __init__(self, scene_runner):
        self.runner = scene_runner

    def start(self):
        # curr_scene = self.runner.start_scene()
        # final_scene = self.runner.final_scene()

        # while curr_scene != final_scene:

        #     curr_scene = curr_scene.get_next_scene()

        curr_scene = self.runner.get_scene("death")

        # Play the final scene
        curr_scene.play()