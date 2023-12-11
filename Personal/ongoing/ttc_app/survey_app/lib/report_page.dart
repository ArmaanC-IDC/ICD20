import 'package:flutter/material.dart';
import 'view_page.dart';

class ReportPage extends StatelessWidget {
  final TextEditingController locationController = TextEditingController();

  ReportPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Report Page'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text('What is the location of the stuff?'),
            const SizedBox(height: 20),
            TextField(
              controller: locationController,
              decoration: const InputDecoration(labelText: 'Location'),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                submitResponse(context);
              },
              child: const Text('Submit'),
            ),
          ],
        ),
      ),
    );
  }

  void submitResponse(BuildContext context) {
    String location = locationController.text.trim();
    if (location.isNotEmpty) {
      // Check if the location is not empty
      // Add the response to the list
      ViewPage.responses.add('Location: $location');
      Navigator.pop(context);
    } else {
      // Handle case where location is empty
      // You can show an error message or take other actions
    }
  }
}
